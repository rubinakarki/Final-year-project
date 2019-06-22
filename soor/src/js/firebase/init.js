import firebase from 'firebase';
import firestore from 'firebase/firestore';

var firebaseConfig = {
    apiKey: "AIzaSyDgKKCk3dMHl2KVo2nmbwsLIZ__atPpAfs",
    authDomain: "chatroom-ed655.firebaseapp.com",
    databaseURL: "https://chatroom-ed655.firebaseio.com",
    projectId: "chatroom-ed655",
    storageBucket: "chatroom-ed655.appspot.com",
    messagingSenderId: "410539977789",
    appId: "1:410539977789:web:53cb7c23f2ee5055"
  };
  // Initialize Firebase
  const firebaseApp = firebase.initializeApp(firebaseConfig);
  firebaseApp.firestore().settings({ timestampsInSnapshots : true })

  export default  firebaseApp.firestore();