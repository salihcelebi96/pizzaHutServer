const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const router = express.Router();

dotenv.config();

mongoose.connect(process.env.MONGODB_URI);

const tatliSchema = new mongoose.Schema({
  tür: {
    type: String,
    required: true,
  },
  fiyat: {
    type: Number,
    required: true,
  },
  url: {
    type: String,
    required: true,
  },
});

const Tatlilar = mongoose.model('tatli', tatliSchema); 

router.get('/', async (req, res) => {
  try {
    const data = await Tatlilar.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post('/', async (req, res) => {
  const { tür, fiyat, url } = req.body;
  try {
    
    const newTatlı = new Tatlilar({
      tür,
      fiyat,
      url,
    });
    const savedTatlı = await newTatlı.save();
    res.status(201).json(savedTatlı);
  } catch (error) {
    console.error('Post işlemi sırasında bir hata oluştu:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

module.exports = router;
