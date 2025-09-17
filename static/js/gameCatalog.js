function addNewRow (tableId, rowData){
    const table = document.getElementById(tableId)
    const name = rowData.gameName;
    const platform = rowData.platform;
    const status = rowData.status;

    const newRow = document.createElement('tr');
    newRow.innerHTML = `
        <td>${name}</td>
        <td>${platform}</td>
        <td>${status}</td>
    `;

    table.appendChild(newRow);
}

async function saveGame(gameForm){
    payload = {"gameName": gameForm.name.value,
               "platform": gameForm.platform.value,
               "status": gameForm.status.value,
               "score": gameForm.ratingStars.value
              }

    try {
        const response = await fetch('/api/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })

        if (!response.ok) {
            return console.error("Erro ao salvar o game:", response.statusText);
        }

        addNewRow('gamesTable', payload); // chama a função que insere a linha

    } catch (e){
        console.log(e)
    }
}