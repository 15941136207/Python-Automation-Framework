
import HTMLTestReportEN


suite = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
if __name__ == '__main__':
    filePath ='F:\\Report.html'
    fp = open(filePath,'wb')
    runner = HTMLTestReportEN.HTMLTestRunner(
        stream=fp,
        title='{ Test Report }',
        #description='',
        #tester="Findyou"
        )
    runner.run(suite())
    
