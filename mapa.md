```mermaid 

graph TD
    A[Manipulación de Imágenes mediante Matrices] --> B[1. Representación Matricial]
    A --> C[2. Operaciones Punto a Punto]
    A --> D[3. Operaciones Espaciales y Convolución]

    %% Nodo 1: Representación
    B --> B1[Estructura de Datos]
    B1 -->|Escala de Grises| B2["Matriz 2D: [Alto x Ancho]"]
    B1 -->|Color BGR / RGB| B3["Matriz 3D: [Alto x Ancho x Canales]"]
    
    B --> B4[Tipos de Datos / Dtype]
    B4 -->|0 a 255| B5["uint8 (Enteros)"]
    B4 -->|Operaciones Matemáticas| B6["float32 / int16 (Previene Overflow)"]

    %% Nodo 2: Operaciones Punto a Punto
    C --> C1["Resta Absoluta: |M1 - M2|"]
    C1 --> C2[Detección de Diferencias Estructurales]
    
    C --> C3[Umbralización / Thresholding]
    C3 --> C4[Aislamiento de Objetos y Binarización]

    %% Nodo 3: Operaciones Espaciales
    D --> D1["Kernel (Matriz de Convolución)"]
    
    D --> D2[Filtrado y Suavizado]
    D2 --> D3[Filtro Gaussiano / Desfoque]
    
    D --> D4[Correlación Cruzada Normalizada - NCC]
    D4 --> D5["Búsqueda de Patrones (Template Matching)"]
    D5 --> D6[Localización de Objetos mediante Picos de Similitud]

    %% Estilos de Nodos
    style A fill:#1f618d,stroke:#154360,stroke-width:2px,color:#fff
    style B fill:#2874a6,stroke:#1b4f72,color:#fff
    style C fill:#2874a6,stroke:#1b4f72,color:#fff
    style D fill:#2874a6,stroke:#1b4f72,color:#fff 
    

