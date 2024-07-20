var Name = ""
var Email = ""
var Password= ""
var Form = document.forms[0]

var query = ""
var created = 0
var delete_ = 0


//table data adding function
function Add(){
    Name = Form[0]
    Email = Form[1]
    Password = Form[2]
    list_names = []
    if (checking(Name,Email,Password)){
        created+=1
        list_names.push(created)
        list_names.push(Name.value)
        list_names.push(Email.value)
        list_names.push(Password.value)
        table = document.querySelector("table")
        row = document.createElement("tr")
        header = document.querySelectorAll("th")
        table.append(row)
        for(let a = 0;a<header.length;a++){
            query = document.createElement("td")
            if (a!=4){
            query.innerHTML =list_names[a]
            row.append(query)}
            else{
                button = document.createElement("button")
                button.setAttribute("class","remove")
                button.setAttribute("onclick","remove_(this)")
            query.append(button)
            button.innerHTML = "Remove"
            row.append(query)}
        }
    
        document.getElementById("Created").innerHTML = "Created rows: "+created
        document.getElementById("Current").innerHTML = "Current row-item: "+(created-delete_)
        document.getElementById("Created").hidden = false
    
    }   
}

// input box clearing function
function Clear(){
    Name.value = ""
    Email.value = ""
    Password.value = ""
}

//Checking function
function checking(Name,Email,Password){
    if (Name.value != "" && Email.value != "" && Password.value != ""){
        return true
} 
    else{
        return false
}
}

    

//remove
function remove_(obj){
obj.parentElement.parentElement.remove()
delete_+=1
document.getElementById("Deleted").innerHTML = "Removed rows: "+delete_
document.getElementById("Deleted").hidden = false
document.getElementById("Current").innerHTML = "Current row-item: "+(created-delete_)
}

