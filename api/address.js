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
    neighborhood: {
        type: String,
        required: true,
    },
    street: {
        type: String,
        required: true,
    },
    addressDetails: {
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
    userEmail: {
        type: String,
        required: true,
    },
    
});

const Address = mongoose.model("address", addressSchema);

router.get("/", async (req, res) => {
    try {
        const data = await Address.find();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" });
    }
});

router.post("/", async (req, res) => {
   const { city, district, neighborhood, street, addressDetails, addressName,userEmail } = req.body;
    try { 
        
        const newAddress = new Address({
           city, 
           district,
           neighborhood, 
           street, 
           addressName,
           addressDetails,
           userEmail,
           
          
            
          });   
          
        const savedNewAddress = await newAddress.save();    
        res.status(201).json(savedNewAddress);
    } catch (error) {
        console.error('Post address işlemi sırasında bir hata oluştu:', error);
        res.status(500).json({ error: "Internal Server Error" });
    }
});        
       

module.exports = router;
