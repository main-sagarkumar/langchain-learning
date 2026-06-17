from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    "data/employee_handbook.pdf"
)

documents = loader.load()

print("Number of documents:", len(documents))

print("\nType of documents:")
print(type(documents))

print("\nType of first document:")
print(type(documents[0]))

for i, doc in enumerate(documents):
    print(f"\n--- PAGE {i+1} ---")
    print(doc.metadata)