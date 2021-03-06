#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehuman.org/

**Code Home Page:**    http://code.google.com/p/makehuman/

**Authors:**           Manuel Bastioni, Marc Flerackers

**Copyright(c):**      MakeHuman Team 2001-2013

**Licensing:**         AGPL3 (see also http://www.makehuman.org/node/318)

**Coding Standards:**  See http://www.makehuman.org/node/165

Abstract
--------

TODO
"""

import numpy as np
import algos3d
import gui3d
import os
import humanmodifier
import events3d
import warp
import mh
import log

class Human(gui3d.Object):

    def __init__(self, mesh, hairObj=None):

        gui3d.Object.__init__(self, [0, 0, 0], mesh, True)
        
        self.warpsNeedReset = True
        self.armature = None
        algos3d.theHuman = self
        
        self.mesh.setCameraProjection(0)
        self.mesh.setShadeless(0)
        self.mesh.setCull(1)
        self.meshData = self.mesh
        
        self.hairModelling = False #temporary variable for easier integration of makehair, will be cleaned later.
        self.hairObj = hairObj
        self.hairProxy = None
        self.clothesObjs = {}
        self.clothesProxies = {}
        self.activeClothing = None
        self.targetsDetailStack = {}  # All details targets applied, with their values
        self.symmetryModeEnabled = False

        self.enableUVInterpolation = 0
        self.targetUVBuffer = {}
        
        self.uvset = None

        self.meshStored = []
        self.meshStoredNormals = []

        self.childVal = 0.0  # child
        self.oldVal = 0.0  # old
        self.youngVal = 1.0
        self.femaleVal = 0.5  # female
        self.maleVal = 0.5  # male
        self.flaccidVal = 0.0
        self.muscleVal = 0.0
        self.overweightVal = 0.0
        self.underweightVal = 0.0
        self.caucasianVal = 1.0/3
        self.asianVal = 1.0/3
        self.africanVal = 1.0/3
        self.dwarfVal = 0.0
        self.giantVal = 0.0
        self.breastSize = 0.0
        self.breastFirmness = 0.5
        self.bodyZones = ['l-eye','r-eye', 'jaw', 'nose', 'mouth', 'head', 'neck', 'torso', 'hip', 'pelvis', 'r-upperarm', 'l-upperarm', 'r-lowerarm', 'l-lowerarm', 'l-hand',
                          'r-hand', 'r-upperleg', 'l-upperleg', 'r-lowerleg', 'l-lowerleg', 'l-foot', 'r-foot', 'ear']
        
        self.setTexture("data/textures/texture.png")        


    # Overriding hide and show to account for both human base and the hairs!

    def show(self):
        self.visible = True
        if self.hairObj:
            self.hairObj.show()
        for obj in self.clothesObjs.values():
            if obj:
                obj.show()
        self.setVisibility(True)
        self.callEvent('onShown', self)

    def hide(self):

        self.visible = False
        if self.hairObj:
            self.hairObj.hide()
        for obj in self.clothesObjs.values():
            if obj:
                obj.hide()
        self.setVisibility(False)
        self.callEvent('onHidden', self)

    # Overriding methods to account for both hair and base object

    def setPosition(self, position):
        dv = [x-y for x, y in zip(position, self.getPosition())]
        gui3d.Object.setPosition(self, position)
        if self.hairObj:
            self.hairObj.setPosition([x+y for x, y in zip(self.hairObj.getPosition(), dv)])
        for obj in self.clothesObjs.values():
            if obj:
                obj.setPosition([x+y for x, y in zip(obj.getPosition(), dv)])
                
        self.callEvent('onTranslated', self)

    def setRotation(self, rotation):
        gui3d.Object.setRotation(self, rotation)
        if self.hairObj:
            self.hairObj.setRotation(rotation)
        for obj in self.clothesObjs.values():
            if obj:
                obj.setRotation(rotation)
                
        self.callEvent('onRotated', self)
            
    def setSolid(self, *args, **kwargs):
        gui3d.Object.setSolid(self, *args, **kwargs)
        if self.hairObj:
            self.hairObj.setSolid(*args, **kwargs)
        for obj in self.clothesObjs.values():
            if obj:
                obj.setSolid(*args, **kwargs)
            
    def setSubdivided(self, *args, **kwargs):
        gui3d.Object.setSubdivided(self, *args, **kwargs)
        if self.hairObj:
            self.hairObj.setSubdivided(*args, **kwargs)
        for obj in self.clothesObjs.values():
            if obj:
                obj.setSubdivided(*args, **kwargs)

    def setGender(self, gender):
        """
        Sets the gender of the model. 0 is female, 1 is male.

        Parameters
        ----------

        amount:
            *float*. An amount, usually between 0 and 1, specifying how much
            of the attribute to apply.
        """

        gender = min(max(gender, 0.0), 1.0)
        self._setGenderVals(gender)
        self.callEvent('onChanging', events3d.HumanEvent(self, 'gender'))

    def getGender(self):
        return self.maleVal

    def _setGenderVals(self, amount):
        if self.maleVal == amount:
            return
        self.maleVal = amount
        self.femaleVal = 1 - amount

    def setAge(self, age):
        """
        Sets the age of the model. 0 if 12 years old, 1 is 70. To set a particular age in years, use the
        formula age_value = (age_in_years - 12) / (70 - 12).

        Parameters
        ----------

        amount:
            *float*. An amount, usually between 0 and 1, specifying how much
            of the attribute to apply.
        """

        age = min(max(age, 0.0), 1.0)
        self._setAgeVals(-1 + 2 * age)
        self.callEvent('onChanging', events3d.HumanEvent(self, 'age'))

    def getAge(self):
        if self.oldVal:
            return 0.5 + self.oldVal / 2.0
        elif self.childVal:
            return 0.5 - self.childVal / 2.0
        else:
            return 0.5

    def _setAgeVals(self, amount):
        if amount >= 0:
            if self.oldVal == amount and self.childVal == 0:
                return
            self.oldVal = amount
            self.childVal = 0
        else:
            if self.childVal == -amount and self.oldVal == 0:
                return
            self.childVal = -amount
            self.oldVal = 0
        self.youngVal = 1 - (self.oldVal + self.childVal)

    def setWeight(self, weight):
        """
        Sets the amount of weight of the model. 0 for underweight, 1 for overweight.

        Parameters
        ----------

        amount:
            *float*. An amount, usually between 0 and 1, specifying how much
            of the attribute to apply.
        """

        weight = min(max(weight, 0.0), 1.0)
        self._setWeightVals(-1 + 2 * weight)
        self.callEvent('onChanging', events3d.HumanEvent(self, 'weight'))

    def getWeight(self):
        if self.overweightVal:
            return 0.5 + self.overweightVal / 2.0
        elif self.underweightVal:
            return 0.5 - self.underweightVal / 2.0
        else:
            return 0.5

    def _setWeightVals(self, amount):
        if amount >= 0:
            if self.overweightVal == amount and self.underweightVal == 0:
                return
            self.overweightVal = amount
            self.underweightVal = 0
        else:
            if self.underweightVal == -amount and self.overweightVal == 0:
                return
            self.underweightVal = -amount
            self.overweightVal = 0

    def setMuscle(self, muscle):
        """
        Sets the amount of muscle of the model. 0 for flacid, 1 for muscular.

        Parameters
        ----------

        amount:
            *float*. An amount, usually between 0 and 1, specifying how much
            of the attribute to apply.
        """

        muscle = min(max(muscle, 0.0), 1.0)
        self._setMuscleVals(-1 + 2 * muscle)
        self.callEvent('onChanging', events3d.HumanEvent(self, 'muscle'))

    def getMuscle(self):
        if self.muscleVal:
            return 0.5 + self.muscleVal / 2.0
        elif self.flaccidVal:
            return 0.5 - self.flaccidVal / 2.0
        else:
            return 0.5

    def _setMuscleVals(self, amount):
        if amount >= 0:
            if self.muscleVal == amount and self.flaccidVal == 0:
                return
            self.muscleVal = amount
            self.flaccidVal = 0
        else:
            if self.flaccidVal == -amount and self.muscleVal == 0:
                return
            self.flaccidVal = -amount
            self.muscleVal = 0

    def setCaucasian(self, caucasian, sync=True):
        caucasian = min(max(caucasian, 0.0), 1.0)
        old = 1 - self.caucasianVal
        self.caucasianVal = caucasian
        if not sync:
            return
        new = 1 - self.caucasianVal
        if old < 1e-6:
            self.asianVal = new / 2
            self.africanVal = new / 2
        else:
            self.asianVal *= new / old
            self.africanVal *= new / old
        self.callEvent('onChanging', events3d.HumanEvent(self, 'caucasian'))
        
    def getCaucasian(self):
        return self.caucasianVal
            
    def setAfrican(self, african, sync=True):
        african = min(max(african, 0.0), 1.0)
        old = 1 - self.africanVal
        self.africanVal = african
        if not sync:
            return
        new = 1 - self.africanVal
        if old < 1e-6:
            self.caucasianVal = new / 2
            self.asianVal = new / 2
        else:
            self.caucasianVal *= new / old
            self.asianVal *= new / old
        self.callEvent('onChanging', events3d.HumanEvent(self, 'african'))
        
    def getAfrican(self):
        return self.africanVal
            
    def setAsian(self, asian, sync=True):
        asian = min(max(asian, 0.0), 1.0)
        old = 1 - self.asianVal
        self.asianVal = asian
        if not sync:
            return
        new = 1 - self.asianVal
        if old < 1e-6:
            self.caucasianVal = new / 2
            self.africanVal = new / 2
        else:
            self.caucasianVal *= new / old
            self.africanVal *= new / old
        self.callEvent('onChanging', events3d.HumanEvent(self, 'asian'))

    def getAsian(self):
        return self.asianVal
            
    def syncRace(self):
        total = self.caucasianVal + self.asianVal + self.africanVal
        if total < 1e-6:
            self.caucasianVal = self.asianVal = self.africanVal = 1.0/3
        else:
            scale = 1.0 / total
            self.caucasianVal *= scale
            self.asianVal *= scale
            self.africanVal *= scale

    def setHeight(self, height):
        height = min(max(height, -1.0), 1.0)
        self._setHeightVals(height)
        self.callEvent('onChanging', events3d.HumanEvent(self, 'height'))

    def getHeight(self):
        if self.giantVal:
            return self.giantVal
        elif self.dwarfVal:
            return -self.dwarfVal
        else:
            return 0.0

    def _setHeightVals(self, amount):
        if amount >= 0:
            if self.giantVal == amount and self.dwarfVal == 0:
                return
            self.giantVal = amount
            self.dwarfVal = 0
        else:
            if self.dwarfVal == -amount and self.giantVal == 0:
                return
            self.dwarfVal = -amount
            self.giantVal = 0
            
    def setDetail(self, name, value):
        if value:
            self.targetsDetailStack[name] = value
        elif name in self.targetsDetailStack:
            del self.targetsDetailStack[name]

    def getDetail(self, name):
        return self.targetsDetailStack.get(name, 0.0)

    def getSymmetryGroup(self, group):
        if group.name.find('l-', 0, 2) != -1:
            return self.mesh.getFaceGroup(group.name.replace('l-', 'r-', 1))
        elif group.name.find('r-', 0, 2) != -1:
            return self.mesh.getFaceGroup(group.name.replace('r-', 'l-', 1))
        else:
            return None

    def getSymmetryPart(self, name):
        if name.find('l-', 0, 2) != -1:
            return name.replace('l-', 'r-', 1)
        elif name.find('r-', 0, 2) != -1:
            return name.replace('r-', 'l-', 1)
        else:
            return None

    def applyAllTargets(self, progressCallback=None, update=True):
        """
        This method applies all targets, in function of age and sex

        **Parameters:** None.

        """        
        algos3d.resetObj(self.meshData)

        if progressCallback:
            progressCallback(0.0)
        progressVal = 0.0
        progressIncr = 0.5 / (len(self.targetsDetailStack) + 1)

        for (targetPath, morphFactor) in self.targetsDetailStack.iteritems():
            algos3d.loadTranslationTarget(self.meshData, targetPath, morphFactor, None, 0, 0)
            
            progressVal += progressIncr
            if progressCallback:
                progressCallback(progressVal)
                
        
        # Update all verts
        self.getSeedMesh().update()
        self.updateProxyMesh()
        if self.isSubdivided():
            self.updateSubdivisionMesh()
            if progressCallback:
                progressCallback(0.7)
            self.mesh.calcNormals()
            if progressCallback:
                progressCallback(0.8)
            if update:
                self.mesh.update()
        else:
            self.meshData.calcNormals(1, 1)
            if progressCallback:
                progressCallback(0.8)
            if update:
                self.meshData.update()
                
        if progressCallback:
            progressCallback(1.0)
            
        self.callEvent('onChanged', events3d.HumanEvent(self, 'targets'))
        
   
    def getPartNameForGroupName(self, groupName):
        for k in self.bodyZones:
            if k in groupName:
                return k
        return None

    def applySymmetryLeft(self):
        """
        This method applies right to left symmetry to the currently selected
        body parts.

        **Parameters:** None.

        """

        self.symmetrize('l')

    def applySymmetryRight(self):
        """
        This method applies left to right symmetry to the currently selected
        body parts.

        **Parameters:** None.

        """

        self.symmetrize('r')

    def symmetrize(self, direction='r'):
        """
        This method applies either left to right or right to left symmetry to
        the currently selected body parts.


        Parameters
        ----------

        direction:
            *string*. A string indicating whether to apply left to right
            symmetry (\"r\") or right to left symmetry (\"l\").

        """

        if direction == 'l':
            prefix1 = 'l-'
            prefix2 = 'r-'
        else:
            prefix1 = 'r-'
            prefix2 = 'l-'

        # Remove current values

        for target in self.targetsDetailStack.keys():
            targetName = os.path.basename(target)

            # Reset previous targets on symm side

            if targetName[:2] == prefix2:
                targetVal = self.targetsDetailStack[target]
                algos3d.loadTranslationTarget(self.meshData, target, -targetVal, None, 1, 0)
                del self.targetsDetailStack[target]

        # Apply symm target. For horiz movement the value must be inverted

        for target in self.targetsDetailStack.keys():
            targetName = os.path.basename(target)
            if targetName[:2] == prefix1:
                targetSym = os.path.join(os.path.dirname(target), prefix2 + targetName[2:])
                targetSymVal = self.targetsDetailStack[target]
                if 'trans-in' in targetSym:
                    targetSym = targetSym.replace('trans-in', 'trans-out')
                elif 'trans-out' in targetSym:
                    targetSym = targetSym.replace('trans-out', 'trans-in')
                algos3d.loadTranslationTarget(self.meshData, targetSym, targetSymVal, None, 1, 1)
                self.targetsDetailStack[targetSym] = targetSymVal
        
        self.updateProxyMesh()        
        if self.isSubdivided():
            self.getSubdivisionMesh()

        mh.redraw()

    def storeMesh(self):
        log.message("Storing mesh status")
        self.meshStored = self.meshData.coord.copy()
        self.meshStoredNormals = self.meshData.vnorm.copy()

    def restoreMesh(self):
        self.meshData.coord[...] = self.meshStored
        self.meshData.vnorm[...] = self.meshStoredNormals
        self.meshData.markCoords(coor=True, norm=True)

    def resetMeshValues(self):
        self.childVal = 0.0
        self.youngVal = 1.0
        self.oldVal = 0.0
        self.femaleVal = 0.5
        self.maleVal = 0.5
        self.flaccidVal = 0.0
        self.muscleVal = 0.0
        self.overweightVal = 0.0
        self.underweightVal = 0.0
        self.caucasianVal = 1.0/3
        self.asianVal = 1.0/3
        self.africanVal = 1.0/3
        self.dwarfVal = 0.0
        self.giantVal = 0.0
        self.breastSize = 0.0
        self.breastFirmness = 0.5
        self.targetsDetailStack = {}
        
        self.setTexture("data/textures/texture.png")
        
        self.callEvent('onChanging', events3d.HumanEvent(self, 'reset'))
        self.callEvent('onChanged', events3d.HumanEvent(self, 'reset'))

    def load(self, filename, update=True, progressCallback=None):
        
        self.resetMeshValues()

        f = open(filename, 'r')

        for data in f.readlines():
            lineData = data.split()

            if len(lineData) > 0 and not lineData[0] == '#':
                if lineData[0] == 'version':
                    log.message('Version %s', lineData[1])
                elif lineData[0] == 'tags':
                    for tag in lineData:
                        log.message('Tag %s', tag)
                elif lineData[0] == 'gender':
                    self.setGender(float(lineData[1]))
                elif lineData[0] == 'age':
                    self.setAge(float(lineData[1]))
                elif lineData[0] == 'muscle':
                    self.setMuscle(float(lineData[1]))
                elif lineData[0] == 'weight':
                    self.setWeight(float(lineData[1]))
                elif lineData[0] == 'caucasian':
                    self.setCaucasian(float(lineData[1]), False)
                elif lineData[0] == 'african':
                    self.setAfrican(float(lineData[1]), False)
                elif lineData[0] == 'asian':
                    self.setAsian(float(lineData[1]), False)
                elif lineData[0] == 'height':
                    self.setHeight(float(lineData[1]))
                elif lineData[0] == 'asymmetry':
                    self.targetsDetailStack['data/targets/asym/' + lineData[1] + '.target'] = float(lineData[2])
                elif lineData[0] in gui3d.app.loadHandlers:
                    gui3d.app.loadHandlers[lineData[0]](self, lineData)
                else:
                    log.message('Could not load %s', lineData)

        f.close()

        self.syncRace()

        self.callEvent('onChanged', events3d.HumanEvent(self, 'load'))

        if update:
            self.applyAllTargets(progressCallback)

    def save(self, filename, tags):
        
        f = open(filename, 'w')
        f.write('# Written by makehuman 1.0.0 alpha 8\n')
        f.write('version 1.0.0\n')
        f.write('tags %s\n' % tags)
        f.write('gender %f\n' % self.getGender())
        f.write('age %f\n' % self.getAge())
        f.write('muscle %f\n' % self.getMuscle())
        f.write('weight %f\n' % self.getWeight())
        f.write('african %f\n' % self.getAfrican())
        f.write('asian %f\n' % self.getAsian())
        f.write('caucasian %f\n' % self.getCaucasian())
        f.write('height %f\n' % self.getHeight())

        for t in self.targetsDetailStack.keys():
            if '/asym' in t:
               f.write('asymmetry %s %f\n' % (os.path.basename(t).replace('.target', ''), self.targetsDetailStack[t]))
               
        for handler in gui3d.app.saveHandlers:
            handler(self, f)
               
        f.close()

