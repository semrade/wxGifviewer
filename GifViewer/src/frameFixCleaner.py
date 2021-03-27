#coding: utf-8 

import os

def cleanFrame(frameCode):
    fbGeneratedCode = frameCode.replace('\t','    ')
    fbGeneratedCode = fbGeneratedCode.replace('m_','')
    fbGeneratedCode = fbGeneratedCode.replace('animate','adv')
    return fbGeneratedCode
    
def fixFrame(ProjectDirectory,filename):
    srcFile = os.path.join(ProjectDirectory+"\descode",filename+'.py')
    framCode=""
    
    # open the file generated by wxformebuilder.
    ptrFile=open(srcFile,'r')
    #-----start cleaning 
    for line in ptrFile:
        if line.startswith('# -*- coding: utf-8 -*-'):
            framCode += "# %s.py" %filename
        elif line.startswith('##'):
            pass
        elif line.startswith('import wx.xrc'):
            pass
        elif line.startswith('class'):
            lineSplit = line.split(' ')
            framName = lineSplit[1]
            framCode += line
        elif line.startswith('\tdef __init__( self, parent )'):
            framCode += "\tdef __init__( self ):\n"
        elif line.startswith('\t\twx.Frame.__init__ '):
            framCode += line.replace('parent','None')
        elif line.startswith('\tdef __del__( self ):'):
            pass        
        elif line.startswith('\t\tpass'):
            framCode +='        # ---------- Add widget program settings\n'
            framCode +='        #self.GifPath = None\n'
            framCode +='        # ---------- Add widget program settings\n'
            framCode +='        self.Show()\n'
            framCode +='        # ---------- Event handlers\n'
        else:
            framCode +=line
                        
    framCode +='if __name__ == "__main__":\n'
    framCode +='    app = wx.App(False)\n'
    framCode +='    frame = %s()\n' % framName
    framCode +='    app.MainLoop()\n'

    #clean the code from spaces and _m    
    framCode = cleanFrame(framCode)
    # ------ end cleaning 
    # ------ start the main loop code copie
    
    # ------ end the main loop code copie
    #fbGeneratedCode = ptrFile.read()

    ptrFile.close()
    #print(framCode)
    # ----- Save src code

    outFile = os.path.join(ProjectDirectory+'\src',filename+'BK.py')
    # Save the file to the source folder
    if os.path.exists(outFile):
        ptrFile=open(outFile,"w")
    else:
        ptrFile=open(outFile,"w+")

    # write cleaned code to src folder.    
    ptrFile.write(framCode)
    ptrFile.close()
    return 'CLEANING DONE!'

dirname = os.path.dirname(__file__)
ProjectDirectory = os.path.join(dirname,"..\\")

#ProjectDirectory = r"C:\Users\STarikUser\Documents\gif-viewer"
filename = "gifviewer"

print('Cleaning file: %sBK.py ===> START CLEANING!' % filename)
outStat = fixFrame(ProjectDirectory,filename)
print('The code has been saved to the src folder %s' % outStat )
