document.addEventListener("DOMContentLoaded", function () {
  const newUserBtn = document.getElementById("newUserBtn");
  const userTableBody = document.getElementById("userTableBody");
  const userModal = document.getElementById("userModal");
  const closeBtn = document.querySelector(".close");
  const saveBtn = document.getElementById("saveBtn");
  const userForm = document.getElementById("userForm");

  let editingRowIndex = null;

  newUserBtn.addEventListener("click", openModal);
  closeBtn.addEventListener("click", closeModal);
  saveBtn.addEventListener("click", saveUser);

  function openModal() {
    userForm.reset();
    editingRowIndex = null;
    userModal.style.display = "block";
  }

  function closeModal() {
    userModal.style.display = "none";
  }

  function saveUser() {
    const name = document.getElementById("name").value;
    const lastName = document.getElementById("lastName").value;
    const age = document.getElementById("age").value;

    if (editingRowIndex !== null) {
      //actualiza la fila existente
      updateTableRow(editingRowIndex, name, lastName, age);
    } else {
      // agrega una nueva fila
      addUserToTable(name, lastName, age);
    }

    closeModal();
  }

  // Para actualizar la tabla
  //!No funciona     //Arreglarlo!!
  function updateTableRow(rowIndex, name, lastName, age) {
    const row = userTableBody.rows[rowIndex];
    row.cells[0].textContent = name;
    row.cells[1].textContent = lastName;
    row.cells[2].textContent = age;
    editingRowIndex = null;
  }

  function addUserToTable(name, lastName, age) {
    const row = userTableBody.insertRow();
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);
    const cell3 = row.insertCell(2);
    const cell4 = row.insertCell(3);

    const rowId = "row_" + Date.now();
    row.id = rowId;

    cell1.textContent = name;
    cell2.textContent = lastName;
    cell3.textContent = age;

    const editBtn = document.createElement("button");
    editBtn.textContent = "Editar";
    editBtn.id = "editBtn";
    editBtn.addEventListener("click", () => openEditModal(rowId));

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Eliminar";
    deleteBtn.id = "deleteBtn";
    deleteBtn.addEventListener("click", () => deleteUser(row));

    cell4.appendChild(editBtn);
    cell4.appendChild(deleteBtn);
  }

  // Ventna para editar
  function openEditModal(rowId) {
    openModal();
    const row = document.getElementById(rowId);
    document.getElementById("name").value = row.cells[0].textContent;
    document.getElementById("lastName").value = row.cells[1].textContent;
    document.getElementById("age").value = row.cells[2].textContent;
    editingRowIndex = rowId; // Usar el ID de la fila en edición
  }

  // Eliminar y advertencia
  function deleteUser(row) {
    if (confirm("¿Estás seguro de que deseas eliminar este usuario?")) {
      const rowId = row.id;
      userTableBody.removeChild(row);
      if (editingRowIndex === rowId) {
        editingRowIndex = null;
      }
    }
  }

  // Data prueba 
  addUserToTable("Kelyn", "Tejada", 25);
  addUserToTable("Jean Carlos", "Arnaud", 30);
});
