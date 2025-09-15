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

async function saveGame(gameForm){
    payload = {"gameName": gameForm.name.value,
               "platform": gameForm.platform.value,
               "status": gameForm.status.value,
               "rating": gameForm.ratingStars.value
              }

    try {
        const response = await fetch('/api/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
    } catch (e){
        console.log(e)
    }
}