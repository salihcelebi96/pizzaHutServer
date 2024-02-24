const express = require('express');
const mongoose = require('mongoose');


const dotenv = require('dotenv');
const router = express.Router(); 










dotenv.config();


mongoose.connect(process.env.MONGODB_URI);
const pizzaSchema = new mongoose.Schema({
  tür: {
    type: String,
    required: true,
  },
  fiyatlar: {
    büyük: {
      type: Number,
      required: true,
    },
    orta: {
      type:  Number,
      required: true,
    },
    küçük: {
      type:  Number,
      required: true,
    },
  },
  url: {
    type: String, 
    required: true,
  },
});

const Pizza = mongoose.model('Pizza', pizzaSchema);

router.get('/', async (req, res) => {
  try {
    const data = await Pizza.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post('/', async (req, res) => {
  console.log(req.body);
  const { url, tür, fiyatlar } = req.body;
  try {
    
    const savedPizza = await Pizza.create({
      tür,
      fiyatlar,
      url,
    });

    res.status(201).json(savedPizza);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error', details: error.message });
  }
});



module.exports = router;