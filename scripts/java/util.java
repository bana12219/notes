/*
 *  @RefreshScope actualiza o refresa los atrivutos @value o environment
 *  reinicializa con los nuevos valores en teimpo real sin tener que reiniciar 
 *  la aplicación
 */
@RefreshScope
@RestController
@Autowired
	@Qualifier("itemRestServiceImpl")
	private ItemService itemService;
	@Value("${configuracion.texto}")
	private String texto;
	@GetMapping("/config")
	public ResponseEntity<?> leerConfig(@Value("${server.port}")String puerto){
		...
@PostMapping("/crear")
	@ResponseStatus(HttpStatus.CREATED)
	public Producto crear(@RequestBody Producto producto) {
		return itemService.save(producto);
	}
	@PutMapping("/editar/{id}")
	@ResponseStatus(HttpStatus.CREATED)
	public Producto editar(@RequestBody Producto producto, @PathVariable Long id) {
		return itemService.update(producto, id);
	}
	@DeleteMapping("/eliminar/{id}")
	@ResponseStatus(HttpStatus.NO_CONTENT)
	public void delete(@PathVariable Long id) {
		itemService.delete(id);
	}
--------------------------------------------------------------------------------------------
/**
 * @EnableEurekaClient no es obligatorio, basta con agregar el 
 * spring starter para que se configure en automático
 * @author anab3z
 *
 */
/*
 * se comenta esta línea al agregar Eureka, puesto que eureka incluye ribbon
 * 
//@RibbonClient(name ="servicio-productos-t")
 * @EnableCircuitBreaker envuelve ribbon y maneja los errores 
 * 
@EnableAutoConfiguration(exclude= {DataSourceAutoConfiguration.class})
se agrega porque al agregar el jar commons para usar entity producto require Datasource, 
sin embargo aquí no se requjiere.
 */
@EnableCircuitBreaker
@EnableEurekaClient
@EnableAutoConfiguration(exclude= {DataSourceAutoConfiguration.class})
@SpringBootApplication
public class UdsServicioItemResttempApplication {
------------------------------------------------------------------------------------------
@Configuration
public class AppConfig {
	/**
	 * Cliente rest para trabajar con el resto de MS
	 * @return
	 */
	@Bean ("restTemplateBean")
	@LoadBalanced
	public RestTemplate registrarRestTemplate() {
		return new RestTemplate();
	}
}
-------------------------------------------------------------------------------------------
@Service("itemRestServiceImpl")
public class ItemServiceImpl implements ItemService{
-------------------------------------------------------------------------------------------
#configuracion del puerto donde se levantara el MS 
#server.port=8002
#configuración dinámica del puerto
server.port=${PORT:0}
#nombre de instancia random
eureka.instance.instance-id=${spring.application.name}:${spring.application.instance_id:${random.value}}
#nombre de la aplicaicon
spring.application.name=servicio-item-t
#configuracion ribbon de las instancias del MS que se va a consumir 
#servicio-productos-t.ribbon.listOfServers=localhost:8001,localhost:9001
#la linea anterior se comenta pues Eureka ya incluye ribbon
#Registro de Servicio en servidor Eureka, opcional solo cuando los Ms están en el mismo servidor
eureka.client.service-url.defaultZone=http://uds-eureka-server:8761/eureka
#configuracion timeout hystrix y ribbon para casos upload
hystrix.commad.default.execution.isolation.thread.timeoutInMilliseconds=80000
ribbon.ConnectTimeout:10000
ribbon.ReadTimeout:30000
#In your configuration:
#
#    ribbon.connectionTimeout is 5000
#    ribbon.readTimeout is 15000
#    ribbon.maxAutoRetries is 0 (default)
#    ribbon.maxAutoRetriesNextServer is 1 (default)
#
#So the hystrixTimeout should be:
#
#(5000 + 15000) * (1 + 0) * (1 + 1) // -> 40000 ms

#configurando Zipkin
#el 100% de las veces se envíe la traza 
spring.sleuth.sampler.probability=1.0
#endpoint de zipkin
spring.zipkin.base-url=http://uds-zipkin-server:9411/
spring.rabbitmq.host=uds-rabbit-server
--------------------------------------------------------------------------------------------------
spring.application.name=servicio-item-t
#nombre o ruta del servidor de configuración
spring.cloud.config.uri=http://uds-config-server:8888
#se configura el profile para saber si el Ms va a correr en dev, pre , pro, se puede tener mas de uno separados por ,
spring.profiles.active=dev
#configuracion Sprin actuator
management.endpoints.web.exposure.include=*
