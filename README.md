# CompSci-NEA

Computer Science Non Exam Assessment for Y12-Y13

As part of the A-level Computer Science syllabus, I must complete a Non Exam Assessment. This entails completing an individual project, that needs to be complex enough to be classed as A-level, and also solve a 'real world problem' (whatever that is [I'm kidding I know]).

To use this program, currently you need to point the command to the location of the original image to be scanned. When you are running the program, it will stop after running each step of the program so that you can see the completion of each step. To continue to the next step of the program you will need to press any button on the keyboard.

The final goal of this project is to create a document scanner that runs over a network, by pointing a browser to a certain ip address on the network. It's possible for me to create a github pages website that could provide the data and frontend for my NEA, however it adds complexity that I don't need to consider at this point in time.

To run the program, you will need to run the python file from the terminal with:
python '[Img_Extraction/Scan.py] --file[Path to your image]'
The above code should get the program to run on any Unix operating system.

As of today (22/12/19) I managed to create a working image scanner, and am now working on building a django site which uses the application as part of the site. I aim to get this done by new years day, but we'll see.

--Kourosh
