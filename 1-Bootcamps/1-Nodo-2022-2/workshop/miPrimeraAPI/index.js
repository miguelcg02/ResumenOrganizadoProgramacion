const express = require("express");
const app = express();

app.use(express.json());

var database = []

// nuestra primera ruta
app.get("/participantes", (req, res) => {
  res.json(database);
});

app.post("/participantes", async (req, res) => {
    const body = req.body;
    database.push(body);
  
    res.status(201).send(body);
});

app.listen(3000, () => console.log("Servidor listo ..."));