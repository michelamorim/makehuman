#!/usr/bin/python
# -*- coding: utf-8 -*-
# We need this for gui controls

import gui3d
import os
import sys
if 'nt' in sys.builtin_module_names:
    sys.path.append('./pythonmodules')
import subprocess
import mh2renderman


class AqsisTaskView(gui3d.TaskView):

    def __init__(self, category):
        gui3d.TaskView.__init__(self, category, 'Aqsis')

        self.sceneToRender = None

        optionsBox = gui3d.GroupBox(self, [10, 80, 9.0], 'Options', gui3d.GroupBoxStyle._replace(height=25+36*3+4+24*1+6))
                                              
        #Sliders                            
        self.shadingRateSlider= gui3d.Slider(optionsBox, value=2, min=0.1, max=10, label = "ShadingRate: %.2f")
        self.samplesSlider= gui3d.Slider(optionsBox, value=2, min=1.0, max=10, label = "Samples: %.2f")
        self.skinOilSlider= gui3d.Slider(optionsBox, value=0.3, min=0.0, max=10, label = "Skin Oil: %.2f")
        
        #Buttons
        self.renderButton = gui3d.Button(optionsBox, 'Render')
            
        @self.shadingRateSlider.event
        def onChanging(value):
            self.app.settings['rendering_aqsis_shadingrate'] = value #Using global dictionary in app for global settings
            
        @self.samplesSlider.event
        def onChanging(value):
            self.app.settings['rendering_aqsis_samples'] = value
            
        @self.skinOilSlider.event
        def onChanging(value):
            self.app.settings['rendering_aqsis_oil'] = value
            
        @self.renderButton.event
        def onClicked(event):
            
            if not self.sceneToRender:
                self.sceneToRender = mh2renderman.RMRScene(self.app)
            self.buildShaders()
            self.sceneToRender.render()
            
    def buildShaders(self):
        
        shaders = ['hairpoly','skin2', 'envlight', 'skinbump', 'scatteringtexture', 'bakelightmap', 'eyeball', 'cornea', 'mixer', 'teeth']
        
        for shader in shaders:
            self.buildShader(shader)
        
    def buildShader(self, shader):
        
        srcPath = os.path.join('data/shaders/aqsis', shader + '.sl')
        dstPath = os.path.join(self.sceneToRender.usrShaderPath, shader + '.slx')
        
        if not os.path.exists(dstPath) or os.stat(srcPath).st_mtime > os.stat(dstPath).st_mtime:
            subprocess.Popen('aqsl %s -o "%s"' % (srcPath, dstPath), shell=True)
    
    def onShow(self, event):
        
        self.renderButton.setFocus()
        gui3d.TaskView.onShow(self, event)

def load(app):
    category = app.getCategory('Rendering')
    taskview = AqsisTaskView(category)

def unload(app):
    pass


