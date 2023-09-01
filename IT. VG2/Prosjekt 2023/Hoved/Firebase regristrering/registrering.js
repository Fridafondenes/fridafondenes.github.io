// document.addEventListener("submit", regBruker);

// function regBruker(evt) {
//   evt.preventDefault();


// }

// Initialize Firebase
const firebaseConfig = {
    apiKey: "AIzaSyDcr1wGnOp4fYskL-ldy82eoE8YmXeLzoo",
    authDomain: "regristrere.firebaseapp.com",
    projectId: "regristrere",
    storageBucket: "regristrere.appspot.com",
    messagingSenderId: "835864054899",
    appId: "1:835864054899:web:fa9bb441609811ae196e06",
    measurementId: "G-33DRN4RXFD"
  };
  
  firebase.initializeApp(firebaseConfig);
  // Initialize Firebase
  // Lager en referanse til databasen
  let db = firebase.firestore();
  
  // Get elements
  const navnInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const telefonInput = document.getElementById('number');

  const registerForm = document.getElementById('formreg');
  

  // Add register event
  registerForm.addEventListener('submit', e => {
    e.preventDefault();
    const name = navnInput.value;
    const email = emailInput.value;
    const telefon = telefonInput.value;
    console.log(email + telefon);

    db.collection("publikum").add({
      "navn": name,
      "epost": email,
      "telefon": telefon
    });

    // firebase.auth().createUserWithEmailAndPassword(email, password)
    //   .then(userCredential => {
    //     console.log('Registered successfully!');
    //     // You can redirect the user to another page here
    //   })
    //   .catch(error => {
    //     console.error(error);
    //     // You can display an error message to the user here
    //   });
  });