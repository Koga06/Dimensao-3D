attribute vec3 aPos;
attribute vec4 aCor;
varying vec4 vCor;
void main(){
  gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
  vCor = aCor;
}