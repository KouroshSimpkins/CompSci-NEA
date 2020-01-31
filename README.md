# CompSci-NEA

Computer Science Non Exam Assessment for Y12-Y13

As part of the A-level Computer Science syllabus, I must complete a Non Exam Assessment. This entails completing an individual project, that needs to be complex enough to be classed as A-level, and also solve a 'real world problem' (whatever that is [I'm kidding I know]).

To use this program, currently you need to point the command to the location of the original image to be scanned. When you are running the program, it will stop after running each step of the program so that you can see the completion of each step. To continue to the next step of the program you will need to press any button on the keyboard.

The final goal of this project is to create a document scanner that runs over a network, by pointing a browser to a certain ip address on the network. It's possible for me to create a github pages website that could provide the data and frontend for my NEA, however it adds complexity that I don't need to consider at this point in time.

To run the program, you will need to run the python file from the terminal with:
python '[Img_Extraction/Scan.py] --file[Path to your image]'
The above code should get the program to run on any Unix operating system.

Currently I have two working Django applications built into a website, one to handle users and one to handle the addition of a file to the server where the website is running. Still trying to figure out how to implement the final project into the Django website, and not really getting anywhere at the moment (15/1/2020), currently considering adding it as a completely new app and working from there, not too sure how it'll work though. 

--Kourosh