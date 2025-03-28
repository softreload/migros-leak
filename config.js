// Uygulama Ayarları
const config = {
  app: {
    name: "TestProject",
    environment: "development",
    domain: "example.com",
    apiVersion: "v1"
  },
  
  // API Bağlantıları (TEST - gerçek değil)
  credentials: {
    aws: {
      accessKey: "AKIAIOSFODNN7EXAMPLE",
      secretKey: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
      region: "us-west-2",
      s3Bucket: "example-data-bucket"
    },
    github: {
      token: "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789",
      webhookSecret: "whsec_8dF9aB2cD3eF4gH5iJ6kL7mN8oP9qR0s"
    },
    stripe: {
      publicKey: "pk_live_51ABcDeFGhIjkLMno0123456789abcdefghijklmnopqrstuvwxyz",
      secretKey: "sk_live_51ABcDeFGhIjkLMno0123456789abcdefghijklmnopqrstuvwxyz"
    },
    firebase: {
      apiKey: "AIzaSyDOCAbC1234567890zyxwvutsrqrstuv",
      projectId: "test-project-123",
      authDomain: "test-project-123.firebaseapp.com"
    }
  },
  
  // Servis Endpoint'leri
  endpoints: {
    userApi: "https://api.example.com/users",
    authService: "https://auth.example.com/oauth/token",
    paymentGateway: "https://payments.example.com/api/process",
    internalApi: "http://internal.example.com/api/v2/data",
    graphqlEndpoint: "https://api.example.com/graphql"
  },
  
  // Mail ayarları
  email: {
    smtpServer: "mail.example.com",
    username: "notifications@example.com",
    password: "SuperSecretPassword123", // TODO: Değiştir
    senderName: "Test Project"
  }
};

module.exports = config;
