import "./App.css";
import 'bootstrap/dist/css/bootstrap.min.css'
import NavBar from './components/NavBar'
import Login from './components/Login'
import Like from './components/Like'
import Post from './components/Post'

function App() {
  return (
    <div className="App">
      <NavBar />
      <Login/>
      <Like/>
      <Post />
    </div>
  );
}

export default App;
