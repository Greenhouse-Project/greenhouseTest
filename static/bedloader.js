function populate() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const bedNum = new Number(urlParams.get('bed'));
    document.main.bedPlot.value = bedNum;
}
function planted() {
    var name = document.main.owner.value;
    var plant = document.main.plant_species.value;
    var bedNum = document.main.bedPlot.value;
    alert("Thanks "+name+" for planting "+plant+" in bed "+bedNum);
}
// For form.html
// function planted() {
//     const queryString = window.location.search;
//     const urlParams = new URLSearchParams(queryString);
//     const bedNum = new Number(urlParams.get('bed'));
//     document.main.bedPlot.value = bedNum;
//     var name = document.main.owner.value;
//     var plant = document.main.plant_species.value;
//     alert("Thanks "+name+" for planting "+plant+" in bed "+bedNum);
// }