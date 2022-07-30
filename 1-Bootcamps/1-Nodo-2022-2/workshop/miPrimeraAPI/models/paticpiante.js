const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const participanteSchema = new Schema({
  nombre: String,
  apellido: String,
  hobbie: String,
});

// Crear el modelo
const participante = mongoose.model("participante", participanteSchema);

module.exports = participante;
