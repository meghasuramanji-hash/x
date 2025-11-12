const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());
app.use(express.json());

const FILE = "patientData.json";

// ✅ Load saved data or create empty file
if (!fs.existsSync(FILE)) {
    fs.writeFileSync(FILE, JSON.stringify([]));
}

// ✅ GET all records
app.get("/records", (req, res) => {
    const data = JSON.parse(fs.readFileSync(FILE));
    res.json(data);
});

// ✅ POST new health record
app.post("/records", (req, res) => {
    const data = JSON.parse(fs.readFileSync(FILE));
    data.push(req.body);
    fs.writeFileSync(FILE, JSON.stringify(data, null, 2));
    res.json({ message: "Record saved!" });
});

// ✅ Server Start
app.listen(7000, () => {
    console.log("✅ Storage Server running on port 7000");
});
