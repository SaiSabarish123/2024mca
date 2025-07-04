var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["Name"] = document.getElementById("Name").value;
  formData["College"] = document.getElementById("college").value;
  formData["Course"] = document.getElementById("course").value;
  return formData;
}
function resetForm() {
  document.getElementById("Name").value = "";
  document.getElementById("College").value = "";
  document.getElementById("Course").value = "";
  selectedRow = null;
}
function insertNewRecord(data) {
  var table = document
    .getElementById("list")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.stuName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.stucoll;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.stucour;
  cell4.innerHTML = `<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}
function onEdit(td)
{if(confirm("Are you upadate your details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("Name").value=selectedRow.cells[0].innerHTML;
document.getElementById("College").value=selectedRow.cells[1].innerHTML;
document.getElementById("Course").value=selectedRow.cells[2].innerHTML;
}
}
function updateRecord(formData)
{
  alert("Your form updated sucessfully.......")
selectedRow.cells[0].innerHTML=formData.Name;
selectedRow.cells[1].innerHTML=formData.College;
selectedRow.cells[2].innerHTML=formData.Course;
}
function onsubmit(td)
{
if(confirm("are you want to delete this record")){
  row=td.parsentElement.parsentElement;
  document.getElementById("list").deleteRow(row.rowIndex);
  resetForm();
}
}
