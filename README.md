# jobmate-proto
Central repository for gRPC Protocol Buffers definitions

## Using Generated Code

### TypeScript
After generating the code, install the required dependencies in your project:
```bash
npm install @bufbuild/protobuf@^2.0.0 @grpc/grpc-js@^1.10.0
```

See [gen/ts/README.md](gen/ts/README.md) for detailed usage instructions.

### Python
Install the required packages:
```bash
pip install grpcio grpcio-tools
```

### Go
The generated Go code has no additional dependencies beyond the standard gRPC packages.
