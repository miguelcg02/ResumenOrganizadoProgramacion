const express = require("express");
const app = express();

app.use(express.json());
const mongoose = require("mongoose");

const uri = `mongodb://mongotesttuya:irIXwlGY9W08ymwJZOfI5CICD1QNHt6C0rJ1KgtrIlRpyTKy6FpXCWsghAaM5lRUCeYvo3lXItvJmMaRxb7k9A==@mongotesttuya.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongotesttuya@`;

mongoose
  .connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("conectado a mongodb"))
  .catch((e) => console.log("error de conexión", e));

const Participante = require("./model/participante.js");

// nuestra primera ruta
app.get("/participantes", async (req, res) => {
  const array = await Participante.find();
  res.status(200).send(array);
});

app.post("/participantes", async (req, res) => {
  const body = req.body;

  const participanteDB = new Participante(body);
  await participanteDB.save();
  res.status(201).send(participanteDB);
});

app.put("/participantes/:id", async (req, res) => {
  const body = req.body;
  await Participante.findOneAndReplace(req.params.id, body);
  res.status(204).send();
});

app.delete("/participantes/:id", async (req, res) => {
  await Participante.findOneAndRemove(req.params.id);
  res.status(204).send();
});

app.listen(3000, () => console.log("Servidor listo ..."));
