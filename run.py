import os
with open(os.path.join("C:\\Users\\Gayathri\\Documents\\GitHub\\gcr_enrollment",'Procfile'), "w") as file1:
    toFile = 'web: sh setup.sh && streamlit run IIITMK.py'
    
    file1.write(toFile)