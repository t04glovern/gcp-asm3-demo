def GenerateConfig(context):
    """Generate YAML resource configuration."""

    name_prefix = context.env['deployment'] + '-' + context.env['name']
    cluster_name = name_prefix
    type_name = name_prefix + '-type'
    k8s_endpoints = {
        '': 'api/v1',
        '-apps': 'apis/apps/v1beta1',
        '-v1beta1-extensions': 'apis/extensions/v1beta1'
    }

    resources = [
        {
            'name': cluster_name,
            'type': 'container.v1.cluster',
            'properties': {
                'zone': context.properties['zone'],
                'cluster': {
                    'name': cluster_name,
                    'initialNodeCount': context.properties['initialNodeCount'],
                    'nodeConfig': {
                        'oauthScopes': [
                            'https://www.googleapis.com/auth/' + s
                            for s in [
                                'compute',
                                'devstorage.read_only',
                                'logging.write',
                                'monitoring'
                            ]
                        ]
                    }
                }
            }
        }
    ]
    outputs = []
    for type_suffix, endpoint in k8s_endpoints.iteritems():
        resources.append({
            'name': type_name + type_suffix,
            'type': 'deploymentmanager.v2beta.typeProvider',
            'properties': {
                'options': {
                    'validationOptions': {
                        'schemaValidation': 'IGNORE_WITH_WARNINGS'
                    },
                    'inputMappings': [{
                        'fieldName': 'name',
                        'location': 'PATH',
                        'methodMatch': '^(GET|DELETE|PUT)$',
                        'value': '$.ifNull('
                                 '$.resource.properties.metadata.name, '
                                 '$.resource.name)'
                    }, {
                        'fieldName': 'metadata.name',
                        'location': 'BODY',
                        'methodMatch': '^(PUT|POST)$',
                        'value': '$.ifNull('
                                 '$.resource.properties.metadata.name, '
                                 '$.resource.name)'
                    }, {
                        'fieldName': 'Authorization',
                        'location': 'HEADER',
                        'value': '$.concat("Bearer ",'
                                 '$.googleOauth2AccessToken())'
                    }]
                },
                'descriptorUrl':
                    ''.join([
                        'https://$(ref.', cluster_name, '.endpoint)/swaggerapi/',
                        endpoint
                    ])
            }
        })
        outputs.append({
            'name': 'clusterType' + type_suffix,
            'value': type_name + type_suffix
        })

    return {'resources': resources, 'outputs': outputs}
