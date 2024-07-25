// Validating Birth date
var DOB = document.querySelector("#Date");
DOB.min = "2000-01-01"
DOB.max = "2010-01-01"
function validationevent(){
    var submit =1;
    var FirstName = document.querySelector("#FirstName");
    var LastName = document.querySelector("#LastName");
    var Phone = document.querySelector("#Phone");
    var Resume = document.querySelector("#Resume");
    var Confirm = document.querySelector("#Confirm");
    var submitbutton = document.querySelector("#submit");
    var arr_components = [FirstName,LastName,Phone,Resume]
    var Errors = ['FirstNameError',"LastNameError","PhoneError","ResumeError"]
    var s = (document.getElementById("Confirm").checked);
    //Required field validation
    for(let a=0;a<arr_components.length-1;a++){
        if(arr_components[a].value == ""){
            submit=0;
            document.querySelector(`#${Errors[a]}`).innerText = "Required Field";
            document.querySelector(`#${Errors[a]}`).style.display = "block";
        }
        else{
            document.querySelector(`h2#${Errors[a]}`).style.display = "none";
        }
    }

    //Validating firstname
    if((/[^a-zA-Z]/g).test(FirstName.value))
    {
        document.querySelector(`#${Errors[0]}`).innerText = "Characters only allowed";
        document.querySelector(`#${Errors[0]}`).style.display = "block";
    }
    // Validating Lastname
    else if((/[^a-zA-Z]/g).test(LastName.value)){
        document.querySelector(`#${Errors[1]}`).innerText = "Characters only allowed";
        document.querySelector(`#${Errors[1]}`).style.display = "block";
    }

  
    // Validating Phone number
    else if((/[^0-9{10}]/g).test(Phone.value)){
        document.querySelector(`#${Errors[2]}`).innerText = "Incorrect mail format";
        document.querySelector(`#${Errors[2]}`).style.display = "block";
    }

    //validating Resume file format
    else if(!(['pdf','docx','doc'].includes(Resume.value.substring(Resume.value.indexOf('.')+1)))){
        document.querySelector(`#${Errors[3]}`).innerText = "Invalid File format";
        document.querySelector(`#${Errors[3]}`).style.display = "block";
    }

    //Validating Resume size
    else if((Resume.files.length==1) && ((Resume.files[0].size)/1000000 > 2.0)){
        document.querySelector(`#${Errors[3]}`).innerText = "Maximum Size limit is 2MB";
        document.querySelector(`#${Errors[3]}`).style.display = "block";
    }

    //Validating Aggrement checkbox
    else if(s == false){
        console.log(document.getElementById("Confirm").checked)
        document.querySelector(`#ConfirmError`).innerText = "Agree conditions and terms";
        document.querySelector(`#ConfirmError`).style = "display:block";
    }
    else{
        if(submit){
            alert("Form is submitted successfully");
            submit=0;
            FirstName.innerText = ""
            LastName.innerText = ""
            Phone.innerText = ""
            Resume.innerText = ""
            Confirm.checked = false
        }
    }
}
