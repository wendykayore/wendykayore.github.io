var landsatMap = document.getElementById("landsat_map");
var tempMap = document.getElementById("temp_map");
var nvdiMap = document.getElementById("nvdi_map");
var smMap = document.getElementById("sm_map");

var landsatLink = document.getElementById("lsLink");
var tempLink = document.getElementById("tempLink");
var nvdiLink = document.getElementById("nvdiLink");
var smLink = document.getElementById("smLink");

function toggleLS() {
    landsatLink.classList.add("active");
    landsatMap.style.display = "block";

    tempMap.style.display = "none";
    nvdiMap.style.display = "none";
    smMap.style.display = "none";

    tempLink.classList.remove("active");
    nvdiLink.classList.remove("active");
    smLink.classList.remove("active");
}

function toggleTemp() {
    tempLink.classList.add("active");
    tempMap.style.display = "block";

    landsatMap.style.display = "none";
    nvdiMap.style.display = "none";
    smMap.style.display = "none";

    landsatLink.classList.remove("active");
    nvdiLink.classList.remove("active");
    smLink.classList.remove("active");
}

function toggleNVDI() {
    nvdiLink.classList.add("active");
    nvdiMap.style.display = "block";

    tempMap.style.display = "none";
    landsatMap.style.display = "none";
    smMap.style.display = "none";

    landsatLink.classList.remove("active");
    tempLink.classList.remove("active");
    smLink.classList.remove("active");
}

function toggleSM() {
    smLink.classList.add("active");
    smMap.style.display = "block";

    tempMap.style.display = "none";
    nvdiMap.style.display = "none";
    landsatMap.style.display = "none";

    landsatLink.classList.remove("active");
    nvdiLink.classList.remove("active");
    tempLink.classList.remove("active");
}