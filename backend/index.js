const express = require("express");
const { spawn } = require("child_process");
const cors = require("cors");
const multer = require("multer");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.static(path.join(__dirname, "public")));

const storage = multer.diskStorage({
  destination: "./public/uploads",
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  },
});

const upload = multer({ storage: storage });

app.get("/", (req, res) => {
  res.send("Server Running");
});

app.post("/test", upload.single("image"), async (req, res) => {


  const image = req.file.path;
  const answerKey = req.body.answerKey;
  const mark = req.body.marks;
  const python = spawn("python", ["omr.py", image, answerKey, mark]);

  python.stdout.on("data", (data) => {
    res.send(data);
  });

  python.stderr.on("error", (e) => {
    console.log(e);
  });

  python.on("close", (code) => {
    console.log("closed");
  });


});

const port = 3000;

app.listen(port, () => {
  console.log("Server Running");
});
