import { Link } from "react-router-dom";

function Layout({ children }) {
  return (
    <>
      <header>
        <Link to="/">Amir</Link>
        <Link to="/">
          <div>
            {/* <PiShoppingCartSimpleBold /> */}
            <h3>ICON</h3>
            {/* {!!state.itemsCounter && <span>{state.itemsCounter}</span>} */}
          </div>
        </Link>
      </header>
      {children}
      <footer>
        <p>Developed for love</p>
      </footer>
    </>
  );
}

export default Layout;
