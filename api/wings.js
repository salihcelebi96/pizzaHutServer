const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');


const router = express.Router(); 





dotenv.config();

mongoose.connect(process.env.MONGODB_URI);

const wingsSchema = new mongoose.Schema({
  tür: {
    type: String,
    required: true,
  },
  Fiyat: {
    type: Number,
    required: true,
  },
  Açıklama: {
    type:String,
    required: true,
  },
  Url: {
    type: String,
    required: true,
  },
});


const Wings = mongoose.model('Wings', wingsSchema);





router.get('/', async (req, res) => {
  try {
    const data = await Wings.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});




router.post('/', async (req, res) => {
  try {
    const { tür, Fiyat, Açıklama,  Url } = req.body;

    const newWings = new Wings({
      tür,
      Fiyat,
      Açıklama,
      Url,
    });

    const savedWings = await newWings.save();
    res.status(201).json(savedWings);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});











module.exports = router;