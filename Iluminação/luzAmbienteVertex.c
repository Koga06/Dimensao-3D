// Isso é usado no VERTEX SHADER

attribute vec3 aPos;   // Posição do vértice
attribute vec4 aCor;   // Cor do vértice
varying vec4 vCor;     // Cor interpolada para o Fragment Shader

// Constante de iluminação ambiente
const float ambientIntensity = 0.3;

void main() {
    // Luz branca para a iluminação ambiente
    vec3 ambientLight = vec3(1.0, 1.0, 1.0);

    // Aplicando a iluminação ambiente na cor original do vértice
    vec3 ambientColor = aCor.rgb * ambientLight * ambientIntensity;

    // Construção da cor final incluindo o canal alfa
    vCor = vec4(ambientColor, aCor.a);

    // Definição da posição do vértice no espaço de clip
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}
