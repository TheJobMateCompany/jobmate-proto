# JobMate Protocol Buffers - TypeScript

Generated TypeScript code from Protocol Buffers definitions.

## Installation

When using these generated files in your project, make sure to install the required dependencies:

```bash
npm install @bufbuild/protobuf@^2.0.0 @grpc/grpc-js@^1.10.0
```

Or with yarn:

```bash
yarn add @bufbuild/protobuf@^2.0.0 @grpc/grpc-js@^1.10.0
```

## Usage

Import the generated types and services in your TypeScript code:

```typescript
import { AuthServiceClient, RegisterRequest } from './proto/auth/v1/service';
import { credentials } from '@grpc/grpc-js';

// Create a client
const client = new AuthServiceClient(
  'localhost:50051',
  credentials.createInsecure()
);

// Make a request
const request: RegisterRequest = {
  email: 'user@example.com',
  password: 'password123',
  firstName: 'John',
  lastName: 'Doe'
};

client.register(request, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Response:', response);
  }
});
```

## Available Services

- **AuthService** - Authentication and user management
- **DiscoveryService** - Job discovery and feed management
- **CoachService** - AI-powered job analysis and cover letter generation
- **TrackerService** - Application tracking and profile management
