#!/usr/bin/python
# -*- coding: utf-8 -*-
# We need this for gui controls

import gui3d
class RenderingSettingTaskView(gui3d.TaskView):

    def __init__(self, category):
        gui3d.TaskView.__init__(self, category, 'Rendering Setting', label='Settings')

        #Rendering resolution
        y=80
        gui3d.GroupBox(self, [10, y, 9.0], 'Resolution', gui3d.GroupBoxStyle._replace(height=25+24*2+6));y+=25
        rendering_width = self.app.settings.get('rendering_width', 800)
        self.width= gui3d.TextEdit(self, [18, y, 9.3], str(rendering_width), gui3d.TextEditStyle._replace(width=112),
            gui3d.intValidator);y+=24
        rendering_height = self.app.settings.get('rendering_height', 600)
        self.height= gui3d.TextEdit(self, [18, y, 9.3], str(rendering_height), gui3d.TextEditStyle._replace(width=112),
            gui3d.intValidator);y+=24
        y+=16
        
        human = self.app.selectedHuman

        #Hair data
        gui3d.GroupBox(self, [10, y, 9.0], 'Hair', gui3d.GroupBoxStyle._replace(height=25+36*4+6));y+=25
        human.hairs.interpolationRadius = self.app.settings.get('hair.interpolationRadius',  human.hairs.interpolationRadius)
        self.clumpRadius = gui3d.Slider(self, position=[10, y, 9.3], value=human.hairs.interpolationRadius, min=0.05,max=0.5,
            label = "Clump radius: %.4f");y+=36
        human.hairs.clumpInterpolationNumber = self.app.settings.get('hair.clumpInterpolationNumber', human.hairs.clumpInterpolationNumber)
        self.clumpChildren= gui3d.Slider(self, position=[10, y, 9.3], value=human.hairs.clumpInterpolationNumber, min=0, max=150,
            label = "Clump children: %d");y+=36
        human.hairs.multiStrandNumber = self.app.settings.get('hair.multiStrandNumber',  human.hairs.multiStrandNumber)
        self.multiStrand= gui3d.Slider(self, position=[10, y, 9.3], value=human.hairs.multiStrandNumber, min=0, max=150,
            label = "Multistrand children: %d");y+=36
        human.hairs.randomness = self.app.settings.get('hair.randomness',  human.hairs.randomness)
        self.randomHair= gui3d.Slider(self, position=[10, y, 9.3], value=human.hairs.randomness, min=0.0, max=0.5,
            label = "Randomness: %.4f");y+=36

        @self.clumpRadius.event
        def onChanging(value):
            human = self.app.selectedHuman
            human.hairs.interpolationRadius = self.clumpRadius.getValue()
            self.app.settings['hair.interpolationRadius'] = human.hairs.interpolationRadius

        @self.clumpChildren.event
        def onChanging(value):
            human = self.app.selectedHuman
            human.hairs.clumpInterpolationNumber = self.clumpChildren.getValue()
            self.app.settings['hair.clumpInterpolationNumber'] = human.hairs.clumpInterpolationNumber
            
        @self.multiStrand.event
        def onChanging(value):
            human = self.app.selectedHuman
            human.hairs.multiStrandNumber = self.multiStrand.getValue()
            self.app.settings['hair.multiStrandNumber'] = human.hairs.multiStrandNumber
        
        @self.randomHair.event
        def onChanging(value):
            human = self.app.selectedHuman
            human.hairs.randomness = self.randomHair.getValue()
            self.app.settings['hair.randomness'] = human.hairs.randomness

        @self.width.event
        def onChange(value):
            self.app.settings['rendering_width'] = 0 if not value else int(value)

        @self.height.event
        def onChange(value):
            self.app.settings['rendering_height'] = 0 if not value else int(value)

    def onHide(self, event):

        gui3d.TaskView.onHide(self, event)
        self.app.saveSettings()

def load(app):
    category = app.getCategory('Rendering')
    taskview = RenderingSettingTaskView(category)
    print 'Rendering setting imported'

def unload(app):
    pass

