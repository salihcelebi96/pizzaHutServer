const express = require('express');
const mongoose = require('mongoose');

const dotenv = require('dotenv');
const router = express.Router();  









dotenv.config();
mongoose.connect(process.env.MONGODB_URI);


const kampanyaSchema = new mongoose.Schema({
  tür: {
    type: String,
    required: true,
  },
  fiyat: {
    type: Number,
    required: true,
  },
  acıklama: {
    type:String,
    required: true,
  },
  image: {
    type: String,
    required: true,
  },
});


const Kampanyalar = mongoose.model('Kampanyalar', kampanyaSchema);





router.get('/', async (req, res) => {
  try {
    const data = await Kampanyalar.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});




module.exports = router;