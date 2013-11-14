import csv
import os
import smtplib
import datetime
import shutil
import sys

class Reporting:
    def __init__(self, reconFile, emailTo, jobNumber, label):      
        self.reconFile = reconFile
        self.emailTo = emailTo
        self.jobNumber = jobNumber
        self.label = label     
        # Initiate counter variables
        self.fileCount = 0
        self.tPackages = 0
        self.tImages   = 0

    def main(self):
        print self.reconFile
        e = Email(self.emailTo)
        header = e.emailHeader(self.emailTo, self.label)
        bodyTemplate = e.emailBodyTemplate()
        jobLines = self.iterateJobList()
        footer = e.emailFooter(self.fileCount, self.tImages, self.tPackages)
        eMsg = header + bodyTemplate + jobLines + footer
        e.sendEmail(eMsg)

    """
    Uses Command line variable does not parse directory.
    """
    def iterateJobList(self):
        jobDetailLine = ""
        with open(self.reconFile,'rb') as csvfile:
            reportreader = csv.reader(csvfile, delimiter='\t')
            for row in reportreader:
                # Cleanse whitespace
                row = [element.strip(' ') for element in row]                
                # Split full job name for columns.
                jobDetailLine += self.jobDetails(row)                          
        return jobDetailLine

    def jobDetails(self, jobDetailsList):
        details = []
        jobLines = ""
        if jobDetailsList and not jobDetailsList[0].startswith("Job"):
            details = [jobDetailsList[0][0:8], jobDetailsList[2],
                       jobDetailsList[4], jobDetailsList[6]]
            self.fileCount += 1
            self.tImages += int(details[2])
            self.tPackages += int(details[3])
            e = Email(self.emailTo)
            jobLines = e.buildJobLine(details, self.jobNumber,
                                      self.fileCount)
        return jobLines

    def formatDate(self, filedate):
        formatDate = datetime.datetime.strptime(filedate, "%Y%m%d").date()
        date = formatDate.strftime("%m/%d/%Y")
        return date


class Email:
    def __init__(self, emailTo):
        self.smtpServer = '127.0.0.1'
        self.sender = """bob <bob@home.com"""
        self.emailTo = emailTo

        
    def emailHeader(self, toList, subject):
        message = ("From: {0}\n"
                   "To: {1}\n"
                   "MIME-Version: 1.0\n"
                   "Content-type: text/html\n"
                   "Subject: {2} Recon Report \n\n").format(self.sender, '; '.join(toList),
                                               subject)
        return message
    
    def emailBodyTemplate(self):
        message =   """<table width='95%'>
            <tr><td colspan='7'></td></tr>
            <tr>
                <td width='10%'><b><u>Job Name</u></b></td>
                <td width='10%'><b><u>Job Number</u></b></td>
                <td width='20%'><b><u>Processed Date</u></b></td>
                <td width='20%'><b><u>Total Images</u></b></td>
                <td width='20%'><b><u>Total Packages</u></b></td>
                <td width='15%'><b><u>Status</u></b></td>
            <tr>

            <style type="text/css">
                tr.0 td {
                    background-color: #ffffff; color: black;
                }
                tr.1 td {
                    background-color: #c1c1c1; color: black;
                }
                td {border: none}
            </style>
        """
        return message

    def buildJobLine(self, jobDetails, jobNumber, rowNumber):
        message = """
                    <tr class ="{5}">
                        <td width='10%'>{0}</td>
                        <td width='10%'>{1}</td>
                        <td width='10%'>{2}</td>
                        <td width='10%'>{3}</td>
                        <td width='10%'>{4}</td>
                        <td width='10%'>Processed</td>
                    </tr>""".format(jobDetails[0], jobNumber, jobDetails[1],
                       jobDetails[2], jobDetails[3], (rowNumber%2))

        return message

    def emailFooter(self, fileCount, tImages, tPackages):
        message = """   </table><hr>
                        <br>File Count: {0}
                        <br>Total Images: {1}
                        <br>Total Packages: {2}""".format(fileCount,
                                                          tImages,
                                                          tPackages)
        return message

    def sendEmail(self, message):
        try:
            smtpObj = smtplib.SMTP(self.smtpServer)
            smtpObj.sendmail(self.sender, self.emailTo, message)
            print "Successfully sent email!"
        except:
            print "Error: unable to send email"
        return


if __name__ == '__main__':
    #Recon file, [emailTo], jobnumber (hardcoded), label

    cmdl = Reporting(sys.argv[1],
                    [r"lil.bob@home.com"],
                    "JOB56789",
                    "These random Files")
    cmdl.main()
