const express = require('express');
const mongoose = require('mongoose');

const dotenv = require('dotenv');
const router = express.Router(); 


dotenv.config();


mongoose.connect(process.env.MONGODB_URI);
const db = mongoose.connection;

db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', function () {
  console.log('MongoDB connected successfully');
});


const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  phoneNumber: String,
  password: String,
  isChecked1: Boolean,
  isChecked2: Boolean,
  isChecked3: Boolean
});

const UserModel = mongoose.model('User', userSchema);







router.post('/', async (req, res) => {
  try {
    const { name, email, phoneNumber, password, isChecked1, isChecked2, isChecked3 } = req.body;
    // Yeni kullanıcı oluştur
    const newUser = new UserModel({ name, email, phoneNumber, password, isChecked1, isChecked2, isChecked3 });
    // Veritabanına kaydet
    const savedUser = await newUser.save();
    res.status(200).json({ message: 'Signup successful', user: savedUser });
  } catch (error) {
    console.error('Error during signup:', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

router.get('/', async (req, res) => {
  try {
    // Tüm kullanıcıları getir
    const users = await UserModel.find({});
    res.status(200).json({ users });
  } catch (error) {
    console.error('Error getting users:', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;
