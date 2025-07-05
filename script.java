
    var selectedRow = null;
    function onFormSubmit() {
      var formData = readFormData();
      if (isValid(formData)) {
        if (selectedRow == null) {
          insertNewRecord(formData);
          alert("Details saved successfully!");
        } else {
          updateRecord(formData);
          alert("Details updated successfully!");
        }
        resetForm();
      } else {
        alert("Please fill all fields correctly.");
      }
    }

    function readFormData() {
      return {
        facName: document.getElementById("facName").value.trim(),
        CorName: document.getElementById("CorName").value.trim(),
        ColName: document.getElementById("ColName").value.trim(),
        facDep: document.getElementById("facDep").value.trim(),
        facSub: document.getElementById("facSub").value.trim(),
        facAge: document.getElementById("facAge").value.trim(),
        facPlace: document.getElementById("facPlace").value.trim()
      };
    }

    function insertNewRecord(data) {
      var table = document.getElementById("faclist").getElementsByTagName("tbody")[0];
      var newRow = table.insertRow();

      newRow.insertCell(0).innerHTML = data.facName;
      newRow.insertCell(1).innerHTML = data.CorName;
      newRow.insertCell(2).innerHTML = data.ColName;
      newRow.insertCell(3).innerHTML = data.facDep;
      newRow.insertCell(4).innerHTML = data.facSub;
      newRow.insertCell(5).innerHTML = data.facAge;
      newRow.insertCell(6).innerHTML = data.facPlace;
      newRow.insertCell(7).innerHTML = `
        <a href="#" onclick="onEdit(this)">Update</a> |
        <a href="#" onclick="onDelete(this)">Delete</a>
      `;
    }

    function resetForm() {
      document.getElementById("facName").value = "";
      document.getElementById("CorName").value = "";
      document.getElementById("ColName").value = "";
      document.getElementById("facDep").value = "";
      document.getElementById("facSub").value = "";
      document.getElementById("facAge").value = "";
      document.getElementById("facPlace").value = "";
      selectedRow = null;
    }

    function onEdit(td) {
      selectedRow = td.parentElement.parentElement;
      document.getElementById("facName").value = selectedRow.cells[0].innerHTML;
      document.getElementById("CorName").value = selectedRow.cells[1].innerHTML;
      document.getElementById("ColName").value = selectedRow.cells[2].innerHTML;
      document.getElementById("facDep").value = selectedRow.cells[3].innerHTML;
      document.getElementById("facSub").value = selectedRow.cells[4].innerHTML;
      document.getElementById("facAge").value = selectedRow.cells[5].innerHTML;
      document.getElementById("facPlace").value = selectedRow.cells[6].innerHTML;
    }

    function updateRecord(formData) {
      selectedRow.cells[0].innerHTML = formData.facName;
      selectedRow.cells[1].innerHTML = formData.CorName;
      selectedRow.cells[2].innerHTML = formData.ColName;
      selectedRow.cells[3].innerHTML = formData.facDep;
      selectedRow.cells[4].innerHTML = formData.facSub;
      selectedRow.cells[5].innerHTML = formData.facAge;
      selectedRow.cells[6].innerHTML = formData.facPlace;
    }

    function onDelete(td) {
      if (confirm("Are you sure you want to delete this record?")) {
        var row = td.parentElement.parentElement;
        document.getElementById("faclist").deleteRow(row.rowIndex);
        resetForm();
      }
    }

    function isValid(data) {
      return (
        data.facName !== "" &&
        data.CorName !== "" &&
        data.ColName !== "" &&
        data.facDep !== "" &&
        data.facSub !== "" &&
        data.facAge !== "" &&
        !isNaN(data.facAge) &&
        parseInt(data.facAge) >= 18 &&
        parseInt(data.facAge) <= 80 &&
        data.facPlace !== ""
      );
    }
  