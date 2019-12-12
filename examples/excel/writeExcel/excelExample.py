from Data.Excel_Utilities.ExcelUtils import updateExcel

sourceURL = '..\..\..\Data\laserJobs_inxls.xls'


updatedJobData = {}
updatedJobData['jobId'] = 11
updatedJobData['Username'] = 'updatedUsername'
updatedJobData['Date'] = 'updatedDate'
updatedJobData['Material'] = 'updatedMaterial'
updatedJobData['Cut_Raster'] = 'updatedCut_Raster'
updatedJobData['Speed'] = 'updatedSpeed'
updatedJobData['Power'] = 'updatedPower'
updatedJobData['DPI'] = 'updatedDPI'
updatedJobData['Freq'] = 'updatedFreq'
updatedJobData['Passes'] = 'updatedPasses'
updatedJobData['RasterDepth'] = 'updatedRasterDepth'
updatedJobData['Others'] = 'updatedOthers'


updateExcel(updatedJobData,sourceURL)





