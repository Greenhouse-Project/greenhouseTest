function planted() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const bedNum = new Number(urlParams.get('bed'));
    document.main.bedPlot.value = bedNum;
    var name = document.main.owner.value;
    var plant = document.main.plant_species.value;
    alert("Thanks "+name+" for planting "+plant+" in bed "+bedNum);
}