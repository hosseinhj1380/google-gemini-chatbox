import { useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
// import Box from "@mui/material/Box";
//

const SearchBox = () => {
  const [jsonData, setJsonData] = useState([]);
  const apiUrl = "http://192.168.20.27:8000/api/v1/rest/chat";

  const postHandler = () => {
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
      body: JSON.stringify({
        message: jsonData,
      }),
    })
      .then((response) => response.json())
      .then((json) => console.log(json));
  };

  return (
    <>
      <div
        sx={{ boxShadow: 0 }}
        style={{
          paddingTop: "10%",
          alignItems: "center",
          justifyContent: "center",
          textAlign: "center",
        }}
      >
        <TextField
          type="text"
          value={jsonData}
          onChange={(e) => setJsonData(e.target.value)}
        />
        <Button onClick={postHandler} variant="outlined">
          Save
        </Button>
        <div>
          <div>{jsonData.response}</div>
          {jsonData && <p>Api Response: {JSON.stringify(jsonData.response)}</p>}
          {/* {<p>API Response: {JSON.stringify(response)}</p>} */}
          {/* {error && <p style={{ color: "red" }}>Error: {error}</p>} */}
        </div>
      </div>
      {/*  */}
    </>
  );
};

export default SearchBox;
