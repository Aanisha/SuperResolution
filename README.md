# Super-Resolution-Image-Project

This is a web-app trained on SRCNN model. On giving an image as input, it reconstructs a higher resolution image of the same.

Note: Only supports .bmp images

## Installation

### To run on Local Host:

<ul><li>Clone the repository</li>
    <li>Open the application.py file, in the folder.</li>
    <li>Change the 
        
        ```UPLOAD_FOLDER = '/app/static/input/'
           OUTPUT_FOLDER = '/app/static/output/'
         ```
           
   to the location of your static/input and static/output folder respectively.</li>
   <li>Save the file.</li>
   <li>Open the terminal, and create a virtual environment inside the application.</li>
   <li>Run the following commands :
     
     ```pip3 install -r requirements.txt```
      
   To install all the modules and dependencies.</li>
   <li>To run the application:
    
           ```python3 application.py```
   </li>
   </ul>
    
    
