const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://127.0.0.1:27017/usermanagement')
  .then(async () => {
    console.log("MongoDB connected successfully");

    // Schema
    const staffSchema = new mongoose.Schema({
      name: String,
      city: String,
      department: String
    });

    // Model
    const Staff = mongoose.model('Staff', staffSchema);
    
    await Staff.create({
      name: "Ravi",
      city: "Hyderabad",
      department: "CSE"
    });
    

    // Read data
    const data = await Staff.find({});
    console.log("Staff Details:", data);

    // Close connection
    mongoose.connection.close();
  })
  .catch(err => console.log(err));
