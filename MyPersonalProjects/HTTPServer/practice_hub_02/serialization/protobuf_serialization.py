
import protobuf_serialization_person_pb2

# Create an instance of the Person message
person_var = protobuf_serialization_person_pb2.Person()
person_var.name = "Alice"
person_var.age = 30
person_var.city = "Blantyre"

# Serialize the message to a compact binary string
serialized_data = person_var.SerializeToString()

# Print the raw bytes (not human-readable)
print(serialized_data)

'''
# protobuf_serialization_person.proto

syntax = "proto3";
message Person {
  string name = 1;
  int32 age = 2;
  string city = 3;
}

# protoc --proto_path=. --python_out=. protobuf_serialization_person.proto

'''