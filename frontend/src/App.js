import "./App.css";
import 'bootstrap/dist/css/bootstrap.min.css'
import NavBar from './components/NavBar'
import Login from './components/Login'
import Like from './components/Like'

function App() {
  return (
    <div className="App">
      <NavBar />
      <Login/>
      <Like/>
    </div>
  );
}

export default App;
