import React, { useEffect, useState } from "react";
import { Alert, Navbar, Button, Container, Col, Row, Form, Table } from "react-bootstrap";
import axios from "axios";

const HomePage = () => {

  const q_1 = [1,2,3,4,5,6,7,8,9,10]
  const q_2 = [11,12,13,14,15,16,17,18,19,20]
  const [answers, setAnswers] = useState([]);
  const [testFile, setTestFile] = useState([]);
  const [results, setResults] = useState([]);
  const [marks, setMarks] = useState(0)

  const onSelect = (event) => {
    setTestFile(event.target.files);
  };

  const evaluate = async () => {

    const fd = new FormData();
    fd.append("image", testFile[0]);
    fd.append("answerKey", JSON.stringify(answers))
    fd.append("marks", marks)
    const config = {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    };
    try {
      const res = await axios.post("http://localhost:3000/test", fd, config);
      const data = res.data
      const data_split = data.split(",")
      const e_code = data_split[0].slice(12,-1)
      const marks = data_split[1].slice(9,-3)
      const temp_result = {}
      temp_result['e_code'] = e_code;
      temp_result['marks'] = marks;
      setResults([...results,temp_result])

    } catch (e) {
      console.log(e);
    }
  };

  const getAnswers = (event) => {
    var selected = false;
    const option = {}
    var nam = event.target.name
    option[nam] = event.target.value
    var ans
    if(answers.length > 0){
      for (ans of answers){
        if (nam in ans){
          ans[nam] = event.target.value
          selected = true
          setAnswers([...answers])
        }
      }
        if(!selected){
          setAnswers([...answers, option])
        }
    }
    else{
      setAnswers([...answers, option])
    }
  } 
 

  const getMarks = (event) => {
    setMarks(event.target.value)
  }

  useEffect(() => {
  },[results, answers])

  return (
    <div className="container">
      <br />
      <Navbar bg="dark" variant="dark" className="center-navbar">
        <Navbar.Brand><h2 >OMR Reader</h2></Navbar.Brand>
      </Navbar>
      <br />

      <Container>
      <h3 variant="primary">Answer Key<span>(Please provide answers)</span></h3>
      
      <br/>
        <Row >
            <Col className="center">
              {q_1.map((q_no, idx) => {
                return(
                  <Form key={idx} onChange={getAnswers}>
                    <Form.Label className="q-no">{q_no}</Form.Label>
                    <Form.Check inline name={q_no} label="A" value="A" type='radio' />
                    <Form.Check inline name={q_no} label="B" value="B" type='radio' />
                    <Form.Check inline name={q_no} label="C" value="C" type='radio' />
                    <Form.Check inline name={q_no} label="D" value="D" type='radio' />
                  </Form>
                )
              })}
            </Col>
          <Col className="center">
          {q_2.map((q_no, idx) => {
                return(
                  <Form key={idx} onChange={getAnswers}>
                    <Form.Label className="q-no">{q_no}</Form.Label>
                    <Form.Check inline name={q_no} label="A" value="A" type='radio' />
                    <Form.Check inline name={q_no} label="B" value="B" type='radio' />
                    <Form.Check inline name={q_no} label="C" value="C" type='radio' />
                    <Form.Check inline name={q_no} label="D" value="D" type='radio' />
                  </Form>
                )
              })}
          </Col>
        </Row>
          <br/>
          <label htmlFor="mark">Mark for Correct Answer</label>
          <input name="mark" type="number" onChange={getMarks} />
      </Container>
          <br/>
    
      <Alert variant="primary">
        <label>Select Test File </label>
        <input onChange={onSelect} name="image" type="file" id="test-files" />

        <Button variant="success"  onClick={evaluate}>
          Evaluate
        </Button>
      </Alert>

      <Alert variant="success">
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Enrollment Code</th>
            <th>Marks</th>
          </tr>
        </thead>
        <tbody>
          {results.map((result, ridx) => {
            return(
              <tr>
                <td>{ridx+1}</td>
                <td>{result.e_code}</td>
                <td>{result.marks}</td>
              </tr>
            )
          })}
          
        </tbody>
</Table>
      </Alert>
    </div>
  );
};

export default HomePage;
