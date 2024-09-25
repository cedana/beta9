package common

import (
	"fmt"
	"net/url"

	"github.com/beam-cloud/beta9/pkg/types"
)

const (
	InvokeUrlTypePath       string = "path"
	InvokeUrlTypeSubdomain  string = "subdomain"
	invokeUrlIgnoreHostname string = "localhost" // Ignore hostname when building local urls
)

func BuildDeploymentURL(externalUrl, invokeUrlType string, stub *types.StubWithRelated, deployment *types.Deployment) string {
	parsedUrl, err := url.Parse(externalUrl)
	if err != nil {
		return ""
	}

	isLocalOrPathBased := parsedUrl.Hostname() == invokeUrlIgnoreHostname || invokeUrlType == InvokeUrlTypePath
	stubConfig, err := stub.UnmarshalConfig()
	isPublic := err == nil && !stubConfig.Authorized

	if isLocalOrPathBased {
		if isPublic {
			return fmt.Sprintf("%s://%s/%s/public/%s", parsedUrl.Scheme, parsedUrl.Host, stub.Type.Kind(), stub.ExternalId)
		}
		return fmt.Sprintf("%s://%s/%s/%s/v%d", parsedUrl.Scheme, parsedUrl.Host, stub.Type.Kind(), deployment.Name, deployment.Version)
	}

	return fmt.Sprintf("%s://%s-v%d.%s", parsedUrl.Scheme, stub.Group, deployment.Version, parsedUrl.Host)
}

func BuildServeURL(externalUrl, invokeUrlType string, stub *types.StubWithRelated) string {
	parsedUrl, err := url.Parse(externalUrl)
	if err != nil {
		return ""
	}

	isLocalOrPathBased := parsedUrl.Hostname() == invokeUrlIgnoreHostname || invokeUrlType == InvokeUrlTypePath

	if isLocalOrPathBased {
		return fmt.Sprintf("%s://%s/%s/id/%s", parsedUrl.Scheme, parsedUrl.Host, stub.Type.Kind(), stub.ExternalId)
	}

	return fmt.Sprintf("%s://%s.%s", parsedUrl.Scheme, stub.ExternalId, parsedUrl.Host)
}