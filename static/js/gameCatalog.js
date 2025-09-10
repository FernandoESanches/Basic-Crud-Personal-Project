function addNewRow (tableId, rowData){
    const name = rowData.name;
    const platform = rowData.platform;
    const status = rowData.status;

    const newRow = document.createElement('tr');
    newRow.innerHTML = `
        <td>${name}</td>
        <td>${platform}</td>
        <td>${status}</td>
    `;

    tableId.appendChild(newRow);
}
