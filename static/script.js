function validateForm() {
    const pregnancies = parseFloat(document.getElementById("pregnancies").value);
    const glucose = parseFloat(document.getElementById("glucose").value);
    const bloodpressure = parseFloat(document.getElementById("bloodpressure").value);
    const skinthickness = parseFloat(document.getElementById("skinthickness").value);
    const insulin = parseFloat(document.getElementById("insulin").value);
    const bmi = parseFloat(document.getElementById("bmi").value);
    const dpf = parseFloat(document.getElementById("dpf").value);
    const age = parseFloat(document.getElementById("age").value);

    if (
        pregnancies < 0 || glucose < 0 || bloodpressure < 0 ||
        skinthickness < 0 || insulin < 0 || bmi < 0 || dpf < 0 || age < 0
    ) {
        alert("Please enter only positive values.");
        return false;
    }

    if (age > 120) {
        alert("Please enter valid age.");
        return false;
    }

    return true;
}