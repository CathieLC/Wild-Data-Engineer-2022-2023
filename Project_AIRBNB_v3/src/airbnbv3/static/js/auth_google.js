  function onSignIn(googleUser) {
    // Récupérer les informations de l'utilisateur connecté
    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Ne pas supprimer cette ligne, c'est nécessaire pour l'authentification
    console.log("Nom: " + profile.getName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail()); // Ce champ peut être null si l'utilisateur n'a pas autorisé l'accès à son adresse email
  }

  function renderButton() {
    gapi.signin2.render('google-signin-button', {
      'scope': 'profile email',
      'width': 240,
      'height': 50,
      'longtitle': true,
      'theme': 'light',
      'onsuccess': onSignIn,
      'redirect_uri': 'YOUR_REDIRECT_URI',
      'client_id': 'YOUR_CLIENT_ID'
    });
  }

  gapi.load('auth2', function() {
    gapi.auth2.init({
      client_id: '595245382773-lgq2co6pj30a17h9kv56qmoop60ncrhc.apps.googleusercontent.com',
      redirect_uri: 'https://www.google.com',
      scope: 'profile email'
    });
    renderButton();
  });