const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

mongoose.connect(process.env.MONGODB_URI);

const addressSchema = new mongoose.Schema({
    addressName: {
        type: String,
        required: true,
    },
    neighbourHood: {
        type: String,
        required: true,
    },
    addressDetail: {
        type: String,
        required: true,
    },
    district: {
        type: String,
        required: true,
    },
    city: {
        type: String,
        required: true,
    },
    user:{
        type: String,
        required: true,
    }
});

const Address = mongoose.model("Address", addressSchema);

router.get("/", async (req, res) => {
    try {
        const data = await Address.find();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" });
    }
});

router.post("/", async (req, res) => {
   const {city,district,neighbourHood, addressDetail, addressName,  user } = req.body;
    try { 
        
        const newAddress = new Address({
           city, 
           district,
           neighbourHood,
           addressDetail,
           addressName,
           user
            
          });   
          const savedNewAddress = await newAddress.save();
            
        res.status(201).json(savedNewAddress);
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" });
    }
});        
       


module.exports = router;
